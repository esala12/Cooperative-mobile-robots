// Generated by gencpp from file dreambot/ControlFeedback.msg
// DO NOT EDIT!


#ifndef DREAMBOT_MESSAGE_CONTROLFEEDBACK_H
#define DREAMBOT_MESSAGE_CONTROLFEEDBACK_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace dreambot
{
template <class ContainerAllocator>
struct ControlFeedback_
{
  typedef ControlFeedback_<ContainerAllocator> Type;

  ControlFeedback_()
    : distance_to_goal(0.0)  {
    }
  ControlFeedback_(const ContainerAllocator& _alloc)
    : distance_to_goal(0.0)  {
  (void)_alloc;
    }



   typedef double _distance_to_goal_type;
  _distance_to_goal_type distance_to_goal;





  typedef boost::shared_ptr< ::dreambot::ControlFeedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::dreambot::ControlFeedback_<ContainerAllocator> const> ConstPtr;

}; // struct ControlFeedback_

typedef ::dreambot::ControlFeedback_<std::allocator<void> > ControlFeedback;

typedef boost::shared_ptr< ::dreambot::ControlFeedback > ControlFeedbackPtr;
typedef boost::shared_ptr< ::dreambot::ControlFeedback const> ControlFeedbackConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::dreambot::ControlFeedback_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::dreambot::ControlFeedback_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::dreambot::ControlFeedback_<ContainerAllocator1> & lhs, const ::dreambot::ControlFeedback_<ContainerAllocator2> & rhs)
{
  return lhs.distance_to_goal == rhs.distance_to_goal;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::dreambot::ControlFeedback_<ContainerAllocator1> & lhs, const ::dreambot::ControlFeedback_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace dreambot

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::dreambot::ControlFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::dreambot::ControlFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dreambot::ControlFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dreambot::ControlFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dreambot::ControlFeedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dreambot::ControlFeedback_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::dreambot::ControlFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "6ad47d3db7202cba81252eaa6fcd95a5";
  }

  static const char* value(const ::dreambot::ControlFeedback_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x6ad47d3db7202cbaULL;
  static const uint64_t static_value2 = 0x81252eaa6fcd95a5ULL;
};

template<class ContainerAllocator>
struct DataType< ::dreambot::ControlFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "dreambot/ControlFeedback";
  }

  static const char* value(const ::dreambot::ControlFeedback_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::dreambot::ControlFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"float64 distance_to_goal  # Feedback - current distance to the goal\n"
"\n"
;
  }

  static const char* value(const ::dreambot::ControlFeedback_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::dreambot::ControlFeedback_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.distance_to_goal);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ControlFeedback_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::dreambot::ControlFeedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::dreambot::ControlFeedback_<ContainerAllocator>& v)
  {
    s << indent << "distance_to_goal: ";
    Printer<double>::stream(s, indent + "  ", v.distance_to_goal);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DREAMBOT_MESSAGE_CONTROLFEEDBACK_H
